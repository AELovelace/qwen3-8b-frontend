# Matrix Functions

GameMaker has a number of functions to deal with matrices, including the matrix\_build\* functions which create a matrix of a certain type, functions to perform matrix math and the functions [matrix\_get](matrix_get.md) and [matrix\_set](matrix_set.md) that allow you to get or set the matrix that's currently used for drawing. Finally, there are the matrix stack functions that can be used, for example, when working with hierarchical transformations (e.g. skeletal animation).

Matrices are very important for many things but are used most in dealing with 3D space, for example they can be used for setting the camera view or for translating or transforming a model.

A list of all matrix functions is given at the bottom of the page (under "Function Reference").

Mini TOC (placeholder)

1. Heading

## Matrices

A matrix is a collection of numbers arranged into a fixed number of rows and columns. Usually the numbers are real numbers, but that doesn't always have to be the case. The following image shows in general how a matrix is constructed with four rows and four columns:

The top row is row 1, the leftmost column is column 1, and this matrix is a 4x4 matrix because it has four rows and four columns (other sized matrices can be constructed). In describing matrices, the format is always rows / columns, and each number that makes up a matrix is called an *element* of the matrix. The elements in a matrix have specific locations, described by their row and column position where the upper\-left corner of the matrix is row 1 column 1\. In the above matrix example, the element at row 1 col 1 is the value 1\. The element at row 2 column 3 is the value 4\.8\.

### Storage

Matrices do not have their own datatype in GameMaker and are stored in [Arrays](../../../GML_Overview/Arrays.md).

 
## Using Matrices

### Creating Matrices

The simplest way to create a matrix is by using the matrix\_build\* functions. These built\-in functions create commonly used matrix types that are used for specific purposes:

mat\_world \= matrix\_build(x, y, 0, 0, 0, direction, 1, 1, 1\);  

 mat\_view \= matrix\_build\_lookat(x, y, z, x \+ lengthdir\_x(1, direction), y \+ lengthdir\_y(1, direction), z, 0, 0, \-1\);  

 mat\_projection \= matrix\_build\_projection\_fov(\-45, view\_wport\[0] / view\_hport\[0], 1, 10000\);

You can also create a matrix yourself directly by creating a 16\-element array. Note, however, that when splitting the initialisation of the matrix over multiple lines, every line represents a column rather than a row:

the\_matrix \=   

 \[  

     1, 0, 0, 0,    // Col 1  

     0, 1, 0, 0,    // Col 2  

     0, 0, 1, 0,    // Col 3  

     x, y, z, 1     // Col 4  

 ];

### Setting Matrices

To set a matrix to be used for drawing you can use [matrix\_set](matrix_set.md). This function sets the matrix of the given type to the value that you pass it. For example:

var \_my\_matrix \= matrix\_build(x, y, z, 0, 0, direction, 1, 1, 1\);  

 matrix\_set(matrix\_world, \_my\_matrix);

When views are enabled, the view and projection matrices for each view are set through the view's camera using [camera\_set\_view\_mat](../../Cameras_And_Display/Cameras_And_Viewports/camera_set_view_mat.md) and [camera\_set\_proj\_mat](../../Cameras_And_Display/Cameras_And_Viewports/camera_set_proj_mat.md):

camera \= view\_camera\[0];  

 mat\_view \= matrix\_build\_lookat(x, y, z, x \+ lengthdir\_x(1, direction), y \+ lengthdir\_y(1, direction), z, 0, 0, \-1\);  

 camera\_set\_view\_mat(camera, mat\_view);  

 mat\_projection \= matrix\_build\_projection\_fov(\-45, 16/9, 1, 10000\);  

 camera\_set\_proj\_mat(camera, mat\_projection);

See: [Cameras And Viewports](../../Cameras_And_Display/Cameras_And_Viewports/Cameras_And_View_Ports.md)

### Matrices In Shaders

The matrices that you set are eventually passed to a shader when GameMaker reaches the drawing part of the current frame. This shader is either a built\-in shader or a custom one.

It is the vertex shader that performs the actual transformation of the positions (as well as the normals, tangents, etc.). For example, GameMaker's default shader takes the 3\-component vertex position of the current vertex, creates a 4\-component vector out of it to allow the multiplication by the 4x4 matrix and then multiplies this vector by the combined transformation of the world, view and projection matrices:

vec4 object\_space\_pos \= vec4(in\_Position, 1\.0\);  

 gl\_Position \= gm\_Matrices\[MATRIX\_WORLD\_VIEW\_PROJECTION] \* object\_space\_pos;

See: [Matrices And Shaders](#matrices_and_shaders)

## Special Matrices

### The Identity Matrix

The **identity matrix** is a special matrix. No change occurs when you multiply a matrix with it. It is the equivalent for matrices of multiplying a number by 1\. You can create an identity matrix using [matrix\_build\_identity](matrix_build_identity.md).

### The Inverse Matrix

The **inverse matrix** is another special matrix. It is the "inverse" of a matrix. Mathematically, the result of multiplying a matrix by its inverse is an identity matrix, similar (though not identical) to how multiplying a number with its inverse (e.g. 5 and 1/5\) is equal to 1\. This matrix can be used to "cancel out" or "undo" the transforms applied by a given matrix. The built\-in function [matrix\_inverse](matrix_inverse.md) returns the inverse matrix of the matrix you pass it. Note that not every matrix has an inverse.

## Types of Matrices

Matrices are mainly used for drawing, to transform the vertices of anything that you draw from local space to the final position on screen. This generally happens in three steps:

    Transform by the world matrix \-\> Transform by the view matrix \-\> Transform by the projection matrix

### Transform matrix

A transform matrix applies one or more transformations to a position. A transformation can be a translation, rotation, scale or a combination of one or more of those.

This type of matrix is created using [matrix\_build](matrix_build.md).

Transforms can be "added" or "concatenated" to create "hierarchies" of transformations, which can be used for skeletal animation.

See: [Transformation Matrices](Matrix_Functions.md#transformation_matrices)

### View matrix

A view matrix converts positions from the game world to the viewpoint of the camera and can be created using [matrix\_build\_lookat](matrix_build_lookat.md).

### Projection matrix

A projection matrix converts positions coming from view space to clip space, after which these new coordinates are transformed to fit the screen or viewport. GameMaker has functions to create two types of projection: an [orthographic](matrix_build_projection_ortho.md) and [perspective](matrix_build_projection_perspective.md) projection.

## Transformation Matrices

This section explains how you can practically use transform matrices in your GameMaker game.

### Coordinate System

Axes and rotations as used in the Room Editor

When you look at the Room Editor, the positive X axis points to the right and the positive Y axis points down. The positive Z axis (depth) points toward the screen. This makes the coordinate system a right\-handed coordinate system (applying the [right\-hand rule](https://en.wikipedia.org/wiki/Right-hand_rule)). Note that, for the coordinate system to be truly right\-handed, the rotations need to be consistent with the ordering of the axes, i.e. positive rotations go from X to Y (clockwise as seen from above), though in GameMaker they are positive going from Y to X instead (counter\-clockwise as seen from above).

  This right\-handed coordinate system with inverted rotations is used on the remainder of this page.

The most straightforward way to set up the projection in GameMaker to be consistent with this is by using a negative FOV and a positive aspect ratio:

mat\_projection \= matrix\_build\_projection\_fov(\-fov\_y, view\_wport\[0] / view\_hport\[0], 1, 10000\);

Together with this, \-Z can be used as "up":

mat\_view \= matrix\_build\_lookat(x, y, z, x \+ lengthdir\_x(1, direction), y \+ lengthdir\_y(1, direction), z, 0, 0, \-1\);

Note that the above setup is not what you have to use and you can use any orientation and "up" axis that you like by using appropriate view and projection matrices.

### What GameMaker normally does

GameMaker normally takes care of transforming the things you draw, moving instances' sprites to their position, possibly rotated and scaled.

Let's look at an instance of an object that has a sprite set. If you haven't added a Draw event to the object, GameMaker performs the default draw, which draws the sprite automatically, at the instance's [x](../../Asset_Management/Instances/Instance_Variables/x.md), [y](../../Asset_Management/Instances/Instance_Variables/y.md), [depth](../../Asset_Management/Instances/Instance_Variables/depth.md), rotated counter\-clockwise by its [image\_angle](../../Asset_Management/Sprites/Sprite_Instance_Variables/image_angle.md) and scaled by its [image\_xscale](../../Asset_Management/Sprites/Sprite_Instance_Variables/image_xscale.md) and [image\_yscale](../../Asset_Management/Sprites/Sprite_Instance_Variables/image_yscale.md):

You can do all of this and a lot more yourself by transforming what you draw using matrices!

### Transformations

A transformation can be one of the following:

| Transform | Description | Visual Result |
| --- | --- | --- |
| Translation | Move to an (x, y, z) position |  |
| Rotation | Rotate around the origin |  |
| Scale | Scale around the origin |  |

The table above shows the basic transformations. In practice, transformations consist of a combination of one or more of these basic transformations that are applied in a specific order.

### Concatenating transformations

To apply multiple transformations one after the other you multiply the matrices of the individual transforms in the reverse order they should be applied; i.e. you *concatenate* the transforms stored in those matrices. The matrix that results from this multiplication applies all transformations.

Draw Event

var \_mat\_transforms\_concatenated \= matrix\_build\_identity();  

  

 var \_mat\_translation \= matrix\_build(x, y, 0, 0, 0, 0, 1, 1, 1\);  

 \_mat\_transforms\_concatenated \= matrix\_multiply(\_mat\_translation, \_mat\_transforms\_concatenated);  // Add translation (last transform to be applied)  

  

 var \_mat\_rotation\_z \= matrix\_build(0, 0, 0, 0, 0, 45, 1, 1, 1\);  

 \_mat\_transforms\_concatenated \= matrix\_multiply(\_mat\_rotation\_z, \_mat\_transforms\_concatenated);   // Add rotation about z (second transform to be applied)  

  

 var \_mat\_scale \= matrix\_build(0, 0, 0, 0, 0, 0, 2, 3, 1\.2\);  

 \_mat\_transforms\_concatenated \= matrix\_multiply(\_mat\_scale, \_mat\_transforms\_concatenated);        // Add scale (first transform to be applied)  

  

 matrix\_set(matrix\_world, \_mat\_transforms\_concatenated);  

 draw\_sprite(sprite\_index, 0, 0, 0\);  

 matrix\_set(matrix\_world, matrix\_build\_identity());
 

  The order of the matrices matters when multiplying matrices. Multiplying a matrix A by a matrix B doesn't give the same result as multiplying matrix B by matrix A.

### Hierarchical Transformations

Once you know how to add transformations by multiplying matrices, you can create multiple "chains" of transformations. One chain of transformations represents, for example, the left arm, another chain represents the right arm, one other chain represents the neck and the head, etc. While you can also do this by multiplying matrices as shown above, this can be done more conveniently using the matrix stack.

## The Matrix Stack

The matrix stack is a stack that stores matrices specifically. It allows for an elegant way of concatenating transformations. The stack works well with recursion and can be used to create skeletal animations.

Pushing onto the stack doesn't push the matrix you pass as the parameter to [matrix\_stack\_push](matrix_stack_push.md), but instead multiplies the matrix at the top of the stack with the one passed and pushes the resulting matrix.

Popping the top matrix from the stack using [matrix\_stack\_pop](matrix_stack_pop.md) removes the transform that was last added, making the previous transform the "current one" again.

The following code example shows a very basic way to use the matrix stack to draw a hierarchical structure:

Create Event

skeleton \= {  

     len: 10,  

     angle: 90,  

     children: \[  

         {  

             len: 20,  

             angle: \-90,  

             children: \[  

                 {  

                     len: 40,  

                     angle: \-90,  

                     children: \[]  

                 }  

             ]  

         },  

         {  

             len: 20,  

             angle: 90,  

             children: \[  

                 {  

                     len: 40,  

                     angle: 90,  

                     children: \[]  

                 }  

             ]  

         },  

         {  

             len: 50,  

             angle: 0,  

             children: \[]  

         }  

     ]  

 };  

  

 draw\_node \= function(\_node)  

 {  

     // Push my transform  

     var \_matrix \= matrix\_build(0, 0, 0, 0, 0, \_node.angle \+ dsin(current\_time \* 0\.1\) \* 30, 1, 1, 1\);  

     matrix\_stack\_push(\_matrix);  

       

     // Draw this node  

     matrix\_set(matrix\_world, matrix\_stack\_top());  

     draw\_line(0, 0, \_node.len, 0\);  

     draw\_circle(\_node.len, 0, 3, false);  

       

     // Now offset  

     \_matrix \= matrix\_build(\_node.len, 0, 0, 0, 0, 0, 1, 1, 1\);  

     matrix\_stack\_push(\_matrix);  

       

     // Draw this node's children  

     array\_foreach(\_node.children, draw\_node);  

       

     // Pop my transforms  

     matrix\_stack\_pop();  

     matrix\_stack\_pop();  

 }
 

Draw Event

var \_mat\_world \= matrix\_build(x, y, 0, 0, 0, 0, 1, 1, 1\);  

 matrix\_stack\_push(\_mat\_world);  

 draw\_node(skeleton);  

 matrix\_stack\_pop();  

 matrix\_set(matrix\_world, matrix\_build\_identity());

In the Create event, a very basic skeleton is first defined as a struct. Every bone is represented by a struct that stores the bone's length, the angle it has relative to its parent bone, and an array of child bones that are also represented by structs that follow the same structure.

Next, a method draw\_node() is defined, which takes any of the previously defined structs. Inside the function a matrix is first created that only performs the bone's rotation. A multiplication with a value derived from [current\_time](../Date_And_Time/current_time.md) is added to do some basic animation. This matrix is then pushed onto the stack. After this, the world matrix is set to the matrix at the top of the stack and a line and circle are drawn to visualise the bone. After that, another transformation that applies the translation to move towards the end (or tail) of the bone is pushed onto the stack. Next, this node's children are drawn by making the function call itself (i.e. recursively). This can be done elegantly with a call to [array\_foreach](../../Variable_Functions/array_foreach.md) and doesn't require a custom function. Finally, the two transforms that were pushed onto the stack before are popped off to keep the stack balanced.

The animation produced by this code looks as follows:

  Always make sure to pop every transform that you push. The number of transforms on the matrix stack is limited to 50.

Note that, similar to concatenating transforms using matrix multiplication, the transform pushed onto the stack last is applied first and the transform pushed onto the stack first is applied last. For example:

// Make sure the stack is cleared  

 matrix\_stack\_clear();  

  

 // Push the last transform to be applied onto the stack  

 var \_mat1 \= matrix\_build(x, y, z, 0, 0, 0, 1, 1, 1\);  

 matrix\_stack\_push(\_mat1\);  

 matrix\_set(matrix\_world, matrix\_stack\_top());  

  

 // Anything drawn here is only transformed by \_mat1  

  

  

 // Push the one before last transform to be applied onto the stack  

 var \_mat2 \= matrix\_build(0, 0, 0, \-90, 0, 0, 1, 1, 1\);  

 matrix\_stack\_push(\_mat2\);  

 matrix\_set(matrix\_world, matrix\_stack\_top());  

  

 // Anything drawn here is transformed by \_mat2, then by \_mat1  

  

  

 // Push the first transform to be applied onto the stack  

 var \_mat3 \= matrix\_build(5, 5, 10, 0, 0, \-30, 1, 1, 1\);  

 matrix\_stack\_push(\_mat3\);  

 matrix\_set(matrix\_world, matrix\_stack\_top());  

  

 // Anything drawn here is transformed first by \_mat3, then by \_mat2, then by \_mat1  

  

  

 // Clear the stack again, also reset the world matrix  

 matrix\_stack\_clear();  

 matrix\_set(matrix\_world, matrix\_build\_identity());
 

## Matrices and Shaders

### Built\-in Matrices

By default, GameMaker sends three matrices to a shader: the world, projection and view matrix. These are the matrices that you set using [matrix\_set](matrix_set.md).

The matrices that you set with [matrix\_set](matrix_set.md) are available through the gm\_Matrices array. Each matrix (world, view, projection) can be used separately, though often you'll want to use the resulting matrix gm\_Matrices\[MATRIX\_WORLD\_VIEW\_PROJECTION] (first transform the vertex by the world matrix, then by the view matrix, then by the projection matrix):

vec4 object\_space\_pos \= vec4(in\_Position, 1\.0\);  

 gl\_Position \= gm\_Matrices\[MATRIX\_WORLD\_VIEW\_PROJECTION] \* object\_space\_pos;

See: [Built\-In Shader Constants](../../Asset_Management/Shaders/Shader_Constants.md)

### Custom Matrices

You can pass your own matrices to a shader as a uniform. For this you can either use [shader\_set\_uniform\_f\_array](../../Asset_Management/Shaders/shader_set_uniform_f_array.md) or [shader\_set\_uniform\_matrix\_array](../../Asset_Management/Shaders/shader_set_uniform_matrix_array.md). In the shader you can define a matrix uniform as follows:

// Single matrix  

 uniform mat4 u\_mMyMatrix;  

  

 // Array of matrices  

 uniform mat4 u\_mMyMatrices\[16];
 

### Projection Matrix Y Flip (OpenGL)

On [OpenGL platforms](#), the OpenGL API uses an inverted Y axis for projection matrices. On such platforms, GameMaker flips the Y axis for projection matrices in all Draw events so the Y axis's direction is consistent with that on non\-OpenGL platforms. However, since this fix is only applied to the Draw events, attempting to use the projection matrix *outside* of Draw events will result in a flipped Y being returned.

## Extending to 3D

The code provided on this page shows how to use matrices to transform anything you like to draw in 2D.

While 3D graphics in its entirety is a very extensive subject, getting your sprites and 3D models out of the flat XY plane and into the third dimension is simple using matrices. To do this you simply add additional rotations about either the X or Y axis.

Since [matrix\_build](matrix_build.md) performs rotations in the order YXZ this can be achieved with a single call to the function:

var \_matrix \= matrix\_build(x, y, depth, \-90, 0, direction, 1, 1, 1\);

The resulting matrix first rotates \-90 degrees about X to turn the instance's sprite upright, then rotates [direction](../../Asset_Management/Instances/Instance_Variables/direction.md) degrees about Z to rotate the sprite in the direction the instance is facing, and finally moves the sprite to the instance's position, taking its depth (its position along the z axis) into account.

## Function Reference

### Modifying Built\-in Matrices

- [matrix\_get](matrix_get.md)
- [matrix\_set](matrix_set.md)

### Matrix Math

- [matrix\_multiply](matrix_multiply.md)
- [matrix\_inverse](matrix_inverse.md)
- [matrix\_transform\_vertex](matrix_transform_vertex.md)

### Building Matrices

- [matrix\_build](matrix_build.md)
- [matrix\_build\_identity](matrix_build_identity.md)
- [matrix\_build\_lookat](matrix_build_lookat.md)
- [matrix\_build\_projection\_ortho](matrix_build_projection_ortho.md)
- [matrix\_build\_projection\_perspective](matrix_build_projection_perspective.md)
- [matrix\_build\_projection\_perspective\_fov](matrix_build_projection_perspective_fov.md)

### Matrix Stack Functions

The following functions are for using a matrix **stack**, which is similar to a [DS Stack](../../Data_Structures/DS_Stacks/ds_stack_create.md), but designed for use only with matrices. This is a handy way to apply multiple matrix operations (like transforms) one after another when creating a 3D scene.

 
- [matrix\_stack\_is\_empty](matrix_stack_is_empty.md)
- [matrix\_stack\_clear](matrix_stack_clear.md)
- [matrix\_stack\_set](matrix_stack_set.md)
- [matrix\_stack\_push](matrix_stack_push.md)
- [matrix\_stack\_pop](matrix_stack_pop.md)
- [matrix\_stack\_top](matrix_stack_top.md)
