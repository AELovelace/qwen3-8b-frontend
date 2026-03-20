# is\_instanceof

This function returns whether the given [struct](../../GML_Overview/Structs.md) is an "instance of" the given [constructor](../../GML_Overview/Structs.md#constr). You can use this function to check if the constructor used to create your struct was the same one as you supplied in the second argument, or if it's a child constructor of your given constructor.

This means that if your struct was created from constructor B, and constructor B is a child of constructor A, calling is\_instanceof(struct\_of\_B, A) will return true.

This function works by checking the [Static Chain](../../GML_Overview/Structs/Static_Structs.md#h) of your given struct to see if your given constructor is included anywhere in that chain. See: [Static Struct](../../GML_Overview/Structs/Static_Structs.md)

  If you use [static\_set](static_set.md) to replace the static chain of a struct, it will modify the behaviour of this function on that struct, as it checks the static chain to determine inheritance. Using [static\_set](static_set.md) is not recommended aside from deserialisation cases where an anonymous struct is loaded back as part of a hierarchy.

 

#### Syntax:

is\_instanceof(struct, constructor)

| Argument | Type | Description |
| --- | --- | --- |
| struct | [Struct](../../GML_Overview/Structs.md) | The struct to check (the "instance") |
| constructor | [Function](../../GML_Overview/Script_Functions.md) | The constructor to check (is the struct an **instance of** this constructor?) |

 

#### Returns:

[Boolean](../../GML_Overview/Data_Types.md)

 

#### Example:
