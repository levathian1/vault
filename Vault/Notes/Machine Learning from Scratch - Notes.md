
Variables: if used to model                            -> target/output variables (dependant)
				if used to model target variables -> predictors/features/input variables (independant)
	quantitative: follow a continuous (or near) scale (height, income ...)
	categorical: discrete values (nation of birth, species type, shirt size ...)

observation: single collection of predictor and target variables
dataset = multiple observations

training dataset    -> used to build model
validation dataset -> compare multiple models
testing dataset      -> evaluate final model

modeling tasks = regression if target is quantitative (not necessarily ordinary least squares linear regression)
						 = classification if target is categorical

## Linear regression

a variable y follows predictor variables x1 through xd, accounting for error rho

### Extensions
- Regularized Regression
- Bayesian Regression
- GLM
