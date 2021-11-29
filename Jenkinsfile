pipeline {
  agent any
  stages {
    stage('Test') {
      steps {
        echo 'Testing..'
        sh 'python -m unittest'
        echo 'Done'
      }
    }
  }
}

