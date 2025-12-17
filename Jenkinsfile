pipeline {
    agent any

    parameters {
        choice(
            name: 'ENV',
            choices: ['dev', 'test', 'prod'],
            description: 'Hangi ortamda deploy edilsin?'
        )
    }

    environment {
        ENV_FILE = ".env.${params.ENV}"
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'master',
                    url: 'https://github.com/USERNAME/REPO.git'
            }
        }

        stage('Build & Deploy') {
            steps {
                sh '''
                docker compose down
                docker compose --env-file ${ENV_FILE} up -d --build
                '''
            }
        }
    }
}