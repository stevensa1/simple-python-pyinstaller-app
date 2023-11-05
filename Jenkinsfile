node {
    checkout scm
    stage('Build') {
        try {
            def pythonImage = docker.image('python:2-alpine')
            pythonImage.inside {
                sh 'python -m py_compile sources/add2vals.py sources/calc.py'
            }
        } catch (Exception e) {
            currentBuild.result = 'FAILURE'
            error "Build failed: ${e.message}"
        }
    }

    stage('Test') {
        try {
            def pytestImage = docker.image('qnib/pytest')
            pytestImage.inside {
                sh 'py.test --verbose --junit-xml test-reports/results.xml sources/test_calc.py'
            }
        } catch (Exception e) {
            currentBuild.result = 'FAILURE'
            error "Test failed: ${e.message}"
        }
        
        junit 'test-reports/results.xml'
    }

    stage('Deliver') {
        try {
            def pyinstallerImage = docker.image('cdrx/pyinstaller-linux:python2')
            pyinstallerImage.inside {
                sh 'pyinstaller --onefile sources/add2vals.py'
            }
        } catch (Exception e) {
            currentBuild.result = 'FAILURE'
            error "Deliver failed: ${e.message}"
        }

        archiveArtifacts 'dist/add2vals'
    }
}