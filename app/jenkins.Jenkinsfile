pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'docker build -t op_demo .'
            }
        }
        stage('Test') {
            steps {
                sh 'docker run op_demo python -m unittest discover'
            }
        }
        stage('SonarQube analysis') {
            steps {
                // Configura SonarQube aquí
            }
        }
    }
}
