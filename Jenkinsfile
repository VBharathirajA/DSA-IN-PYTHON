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
      
    }
}
