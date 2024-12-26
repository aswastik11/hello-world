pipeline{
    agent any
    
    stages{
        stage('Clone Code') {
            steps {
                git url:'https://github.com/aswastik11/hello-world.git'
            }
        }
        stage("Build Image and Push"){
            steps{
                withCredentials([usernamePassword(
                    credentialsId:"dockerHubCred",
                    usernameVariable:"dockerHubUser", 
                    passwordVariable:"dockerHubPass")]){
                sh 'echo $dockerHubPass | docker login -u $dockerHubUser --password-stdin'
                sh "docker image tag node-app:latest ${env.dockerHubUser}/node-app:latest"
                sh "docker push ${env.dockerHubUser}/node-app:latest"
                }
            }
        }
    }
}
