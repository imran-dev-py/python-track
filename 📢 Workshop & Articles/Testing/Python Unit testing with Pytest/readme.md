# Unit testing

> ## Unit tests are not preventing bugs, unit test are for writing clean &maintainable code with confidence

### Types of tests

- Unit tests
	- Test 'isolated units'
		- method or function
	- super high coverage
	- most of the tests
- Integration tests
	- Combine units & tests them together
	- fill in the cracks between tests
- System tests
	- test with everything plugged together and configured as expected
	- from the end user's perspective
- Acceptance tests
	- test the customer's use cases.

### Coverage

- Statement coverage
- Decision coverage
- Condition coverage 

### What are unit tests good for

- finding bug during development
- a design tool
- writing maintainable code
- documenting a developer's intention
- running quickly

### Test structure

- define your inputs and pre-conditions
- invoke the thing
- verify that it did what you expected