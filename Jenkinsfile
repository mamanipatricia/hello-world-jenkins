
pipeline {
    agent any
    parameters {
        string(name: 'repoName', description: 'Type Helm Repo Name to list the artifacts to remove', defaultValue: 'xtime-helm-local')
        string(name: 'itemName', description: 'Type Helm Item Name to remove', defaultValue: 'consumer' )
    }

    stages {
        stage('List_Helm_artifacts_to_remove') {
            when {
                expression { params.repoName != '' && params.itemName != '' }
            }
            steps {
                script {
                    sh "ls"
                    sh "pwd"
                    sh "/usr/bin/python --version"
                    sh "./test.sh"
                    // def cmdArray = ["python", "./remove-artifacts.py", params.repoName, params.itemName, env.ARTIFACTORY_API_KEY]
                    // def proc = cmdArray.execute()
                    // proc.waitFor()
                    // println "finished...!"
                    // println "return code: ${ proc.exitValue()}"
                    // println "stderr: ${proc.err.text}"
                    // println "stdout: ${proc.in.text}"
                }
            }
        }

    }
}

// timeout(time: 2, unit: “HOURS”) {
    // input message: ‘Approve Deploy?’, ok: ‘Yes’
// }


// pipeline {
//     agent { docker { image 'python:3.10.1-alpine' } }
//     stages {
//         stage('build') {
//             steps {
//                 sh 'python --version'
//             }
//         }
//     }
// }