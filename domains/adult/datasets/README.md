# Adult

Predict whether income exceeds $50000/year based on census data. Also known as *Census Income* dataset.

## Attributes

### Original Dataset

| Meaning         | Values                                                       |
| --------------- | ------------------------------------------------------------ |
| income          | <=50K, >50K                                                  |
| age             | continuous                                                   |
| work class      | Private, Self-emp-not-inc, Self-emp-inc, Federal-gov, Local-gov, State-gov, Without-pay, Never-worked |
| sample weight   | continuous                                                   |
| education       | Bachelors, Some-college, 11th, HS-grad, Prof-school, Assoc-acdm, Assoc-voc, 9th, 7th-8th, 12th, Masters, 1st-4th, 10th, Doctorate, 5th-6th, Preschool |
| education level | continuous                                                   |
| marital status  | Married-civ-spouse, Divorced, Never-married, Separated, Widowed, Married-spouse-absent, Married-AF-spouse |
| occupation      | Tech-support, Craft-repair, Other-service, Sales, Exec-managerial, Prof-specialty, Handlers-cleaners, Machine-op-inspct, Adm-clerical, Farming-fishing, Transport-moving, Priv-house-serv, Protective-serv, Armed-Forces |
| relationship    | Wife, Own-child, Husband, Not-in-family, Other-relative, Unmarried |
| race            | White, Asian-Pac-Islander, Amer-Indian-Eskimo, Other, Black  |
| sex             | Female, Male                                                 |
| capital gain    | continuous                                                   |
| capital loss    | continuous                                                   |
| hours per week  | continuous                                                   |
| native country  | United-States, Cambodia, England, Puerto-Rico, Canada, Germany, Outlying-US(Guam-USVI-etc), India, Japan, Greece, South, China, Cuba, Iran, Honduras, Philippines, Italy, Poland, Jamaica, Vietnam, Mexico, Portugal, Ireland, France, Dominican-Republic, Laos, Ecuador, Taiwan, Haiti, Columbia, Hungary, Guatemala, Nicaragua, Scotland, Thailand, Yugoslavia, El-Salvador, Trinadad&Tobago, Peru, Hong, Holand-Netherlands |

### Preprocessed Dataset

Code for preprocessing data can be found in *preprocess.py*. Some features have been removed, other merged, and categorical encoded as labels.

| Meaning         | Values                                           |
| --------------- | ------------------------------------------------ |
| income          | 0, 1                                             |
| age             | continuous                                       |
| work class      | 0, 1, 2, 3                                       |
| education level | continuous                                       |
| marital status  | 0, 1, 2, 3, 4, 5, 6, 7                           |
| occupation      | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 |
| relationship    | 0, 1, 2, 3, 4, 5, 6                              |
| race            | 0, 1, 2, 3, 4                                    |
| sex             | 0, 1                                             |
| capital gain    | continuous                                       |
| capital loss    | continuous                                       |
| hours per week  | continuous                                       |

#### Removed Features

* sample weight: represents the expected number of people represented by the sample, not relevant for classification
* education: duplicate of *education level*
* native country: most samples are from United States of America

#### Merged Values

* work class: *self employed* have been merged regardless of *-inc/-not-inc*; *government* have been merged regardless of *-federal/-local/-state*, *never-worked* has been included in *without-pay*

#### Removed Samples

Every sample exhibiting missing features was removed