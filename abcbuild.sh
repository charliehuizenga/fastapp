#!/bin/sh

# curl function to retrieve abc source files
getabc () {
  curl -O -s https://$GITHUBAUTH@raw.githubusercontent.com/CenterForTheBuiltEnvironment/ABCmodel/65node/model/$1
}

echo Starting download... KeyValue.h included

# download files
getabc abc_main.cpp
getabc abc_65.cpp
getabc abc_json.cpp
getabc json.hpp
getabc abc.cpp
getabc abc.h
getabc abc_bodybuilder.cpp
getabc abc_bodybuilder.h
getabc abc_clothing_ensembles.cpp
getabc abc_utils.cpp
getabc abc_utils.h
getabc ComfortCalculator.cpp
getabc ComfortCalculator.h
getabc LocalSensationOrderProcessor.cpp
getabc LocalSensationOrderProcessor.h
getabc OverallSensationCalculator.cpp
getabc OverallSensationCalculator.h
getabc LocalSensationRole.h
getabc SegmentOutputTypes.h
getabc SensationConstant.h
getabc SensationItem.h
getabc SimComfortResult.h
getabc SimResults.h
getabc ComfortCalculatorCoefficients.h
getabc KeyValue.cpp
getabc KeyValue.h

echo compiling abc...

# compile abc
g++ -o abcmodel abc_main.cpp abc.cpp abc_65.cpp abc_bodybuilder.cpp abc_clothing_ensembles.cpp abc_json.cpp abc_utils.cpp ComfortCalculator.cpp LocalSensationOrderProcessor.cpp OverallSensationCalculator.cpp KeyValue.cpp 
