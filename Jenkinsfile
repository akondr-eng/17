pipeline {
    agent any

    stages {
        stage('Установка зависимостей') {
            steps {
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Тестирование') {
            steps {
                bat 'python -m pytest -v --junitxml=test-report.xml'
            }
        }

        stage('Создание архива') {
            steps {
                bat 'python -m zipfile -c shipping-module.zip shipping.py CHANGELOG.md'
            }
        }
    }

    post {
        always {
            junit allowEmptyResults: true,
                  testResults: 'test-report.xml'
        }

        success {
            archiveArtifacts artifacts: 'shipping-module.zip',
                             fingerprint: true
        }
    }
}
