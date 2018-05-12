## Setup

### Install appium, appium-doctor
`yarn add --dev appium appium-doctor`

### Run appium doctor
`yarn run appium-doctor`

- You will need to fix any errors `appium-doctor` throws.

### Install virtualenv
`pip install --user virtualenv`

### Setup virtualenv
```
virtualenv venv
source venv/bin/activate
```

### Install Python dependencies
`pip install -r requirements.txt`


## Run Tests
- Start Android emulator

### Start appium server
`yarn run appium`

### Start React Native dev server
`react-native start`

### Run E2E tests
`yarn test`