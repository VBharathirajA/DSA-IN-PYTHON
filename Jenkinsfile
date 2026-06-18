pipeline{
    agent any
    stages{
        stage('Build') {
            steps{
                git branch:'main',
                url:'https://github.com/VBharathirajA/DSA-IN-PYTHON.git'
            }
        }
        stage ('test') {
            steps{
                bat 'python DSA/Tree.py'
            }
        }
        stage ('deploy') {
            steps{
                echo " deploying"
            }
        }
        stage('Email'){
            steps{
                mail bcc: '', body: 'i am aspiring cloud enginner with deep focus on aws, devops, python automatio. i recently developed python script using boto3 api to automate aws services like ec2 instance.', cc: '', from: '', replyTo: '', subject: 'application', to: 'bharathirajavishnudevan@gmail.com'
            }
        }
    }
}
