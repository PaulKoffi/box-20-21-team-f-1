#!/bin/bash
# cd steps
sleep 20
behave triggerAnomaly.feature
behave abortedLaunch.feature
behave destructionBeforeSeparation.feature
behave everythingIsGoingWell.feature
behave destructionAfterSeparation.feature