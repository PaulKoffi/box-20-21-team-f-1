#!/bin/bash
# cd steps
sleep 20
behave triggerAnomaly.feature
behave abortedLaunch.feature
behave destructionBeforeLaunch.feature
behave everythingIsGoingWell.feature
behave destructionAfterLaunch.feature