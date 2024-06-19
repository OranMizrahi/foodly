pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    docker.build('oranmz/foodly:latest')
                    docker.withRegistry('https://index.docker.io/v1/', 'dockerhub-credentials') {
                        docker.image('oranmz/foodly:latest').push('latest')
                    }
                }
            }
        }
    }
}