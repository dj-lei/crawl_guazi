pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                sh 'printenv'
                sh 'docker rmi crawl/guazi:latest'
                sh 'docker build . -t crawl/guazi:latest'
            }
        }
        stage('deploy') {
            steps {
                sh 'docker run -u root --rm --name my-crawl crawl/guazi'
            }
        }
    }
}