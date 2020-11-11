Rocket simulation: 
    (For payload)
    topic: launcherTopic 
    data format min:    
        { 'action' : Stage separation,
          'siteName' : siteName,
          'rocketName' : rocketName
        }
        action: "Stage separation"

    
    topic: rocketTopic
    data format min { 'action' : RUNNING,
                    'siteName' : siteName,
                    'rocketName' : rocketName, 
                    'state': str(statesArray[index])}