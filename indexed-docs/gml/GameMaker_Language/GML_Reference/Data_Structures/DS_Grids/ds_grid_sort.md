# ds\_grid\_sort

This function can be used to sort a DS grid based on the values from a given column (much as you would sort files by date, size etc... in the OS file explorer). The following image shows an example:

 

#### Syntax:

ds\_grid\_sort(index, column, ascending)

| Argument | Type | Description |
| --- | --- | --- |
| index |  | The handle of the grid to sort. |
| column |  | The column to use for sorting the rows |
| ascending |  | Whether to sort lowest to highest (true), or highest to lowest (false). |

 

#### Returns:

 

#### Example:

ds\_grid\_sort(grid, 3, false)

This would take all the values in the DS grid indexed in the variable "grid" and sort them according to the values found in the 3rd column of the grid (as shown in the above image).
