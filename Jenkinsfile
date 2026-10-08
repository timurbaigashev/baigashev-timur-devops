pipeline {
    agent any

    environment {
        STUDENT_NAME = 'Timur'
        STUDENT_SURNAME = 'Baigashev'
        STUDENT_GROUP = 'IT2-2312'
        STUDENT_ID = '37540'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
                sh 'echo "Student: ${STUDENT_NAME} ${STUDENT_SURNAME}"'
                sh 'echo "Group: ${STUDENT_GROUP}"'
                sh 'echo "Student ID: ${STUDENT_ID}"'
            }
        }

        stage('Build') {
            steps {
                sh 'chmod +x scripts/Baigashev_Timur_system.sh'
            }
        }

        stage('Test') {
            steps {
                sh './scripts/Baigashev_Timur_system.sh'
            }
        }

        stage('Docker Build') {
            steps {
                sh 'docker build -t baigashev-timur-devops .'
            }
        }

        stage('Docker Run') {
            steps {
                sh 'docker stop baigashev-timur-container || true'
                sh 'docker rm baigashev-timur-container || true'
                sh '''
                    docker run -d \
                      -p 8080:8080 \
                      -e STUDENT_NAME="${STUDENT_NAME}" \
                      -e STUDENT_SURNAME="${STUDENT_SURNAME}" \
                      -e STUDENT_GROUP="${STUDENT_GROUP}" \
                      -e STUDENT_ID="${STUDENT_ID}" \
                      --name baigashev-timur-container \
                      baigashev-timur-devops
                '''
            }
        }
    }
}
