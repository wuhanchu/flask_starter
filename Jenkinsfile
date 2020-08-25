pipeline {
    triggers {
        pollSCM ('* * * * *')
    }

    agent {
        label 'master'
    }

    environment {
        GROUP = "flask_starter"
        PROJECT = "flask_starter_server"

        // SERVER_DEV = "192.168.1.150"
        // PORT_DEV  = "32032"
        // PROXY_SERVER_DEV = "http://172.17.0.1:32025"
        // SQLALCHEMY_DATABASE_URI_DEV = "postgresql://postgres:dataknown1234@172.17.0.1:32021/dataknown"

        // SERVER_TEST = "172.17.0.1"
        // PORT_TEST  = "31036"
        // SQLALCHEMY_DATABASE_URI_TEST = "postgresql://postgres:dataknown1234@172.17.0.1:31014/dataknown"
        // PROXY_SERVER_TEST = "http://172.17.0.1:31041"
    }

    stages {
        stage('READY') {
            steps{
                withDockerRegistry(registry: [url: "https://server.aiknown.cn:31003", credentialsId: 'harbor']) {
                    sh 'echo ${BRANCH_NAME}'
                    sh 'echo ${TAG_NAME}'
                    sh 'docker pull server.aiknown.cn:31003/z_ai_frame/alpine-python3:latest'
                }
            }
        }

        stage('Docker Build') {
            parallel {
                stage('Docker Build Branch') {
                     when {
                         anyOf {

                            branch 'master'
                            branch 'develop'
                        }
                    }
                    steps{
                        sh 'docker build . -f ./Dockerfile  -t server.aiknown.cn:31003/${GROUP}/${PROJECT}:${BRANCH_NAME}'
                    }
                }

                stage('Docker Build Tag') {
                    when { buildingTag()}
                    steps{
                        sh 'docker build . -f ./Dockerfile  -t server.aiknown.cn:31003/${GROUP}/${PROJECT}:${TAG_NAME}'
                    }
                }
            }
        }

        stage('Push') {
            when {
              expression {
                currentBuild.result == null || currentBuild.result == 'SUCCESS'
              }
            }

            parallel {
                stage('Push Branch') {
                    when {
                         anyOf {
                            branch 'master'
                            branch 'develop'
                        }
                    }
                    steps {
                        withDockerRegistry(registry: [url: "https://server.aiknown.cn:31003", credentialsId: 'harbor']) {
                            sh 'docker push server.aiknown.cn:31003/${GROUP}/${PROJECT}:${BRANCH_NAME}'
                            sh 'docker rmi server.aiknown.cn:31003/${GROUP}/${PROJECT}:${BRANCH_NAME}'
                        }
                    }
                }

                stage('Push Tag') {
                    when { buildingTag() }

                    steps{
                        withDockerRegistry(registry: [url: "https://server.aiknown.cn:31003", credentialsId: 'harbor']) {
                            sh 'docker push server.aiknown.cn:31003/${GROUP}/${PROJECT}:${TAG_NAME}'
                            sh 'docker rmi server.aiknown.cn:31003/${GROUP}/${PROJECT}:${TAG_NAME}'
                        }
                    }
                }
            }
        }

        stage('Deploy') {
            parallel {
                stage('Deploy Develop') {
                    when {
                        branch 'develop'
                     }

                    steps {
                        sshagent(credentials : ['dataknown_dev']) {
                             sh "ssh  -t  root@${SERVER_DEV} -o StrictHostKeyChecking=no  'docker pull server.aiknown.cn:31003/${GROUP}/${PROJECT}:${BRANCH_NAME} &&  docker rm -f  ${PROJECT}; docker run --restart=always -d -p ${PORT_DEV}:5000    -e PROXY_SERVER_URL=${PROXY_SERVER_DEV}  -e SQLALCHEMY_DATABASE_URI=${SQLALCHEMY_DATABASE_URI_DEV}   --name ${PROJECT} server.aiknown.cn:31003/${GROUP}/${PROJECT}:${BRANCH_NAME};'"
                        }
                    }
                }

                stage('Deploy Test') {
                    when {
                        branch 'master'
                     }

                    steps {
                        sshagent(credentials : ['dataknown_test']) {
                             sh "ssh  -t  root@${SERVER_TEST} -o StrictHostKeyChecking=no  'docker pull server.aiknown.cn:31003/${GROUP}/${PROJECT}:${BRANCH_NAME} &&  docker rm -f  ${PROJECT}; docker run --restart=always -d -p ${PORT_TEST}:5000   -e PROXY_SERVER_URL=${PROXY_SERVER_TEST} -e SQLALCHEMY_DATABASE_URI=${SQLALCHEMY_DATABASE_URI_TEST} --name ${PROJECT} server.aiknown.cn:31003/${GROUP}/${PROJECT}:${BRANCH_NAME};'"
                        }
                    }
                }
            }
        }
    }
}
