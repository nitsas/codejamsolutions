#!/bin/bash
# Quickly initialize a problem directory with templates and helpful files.


# did we get all 4 input parameters we expected?
if [ $# -ne 4 ]
then
  echo 'Usage: init_problem.sh "Problem Name" Year "Round" Link'
  exit 0
fi


# read input parameters into vars
name=${1:-DefaultProblemName}
year=${2:-DefaultYear}
round=${3:-DefaultRound}
link=${4:-DefaultLink}
date=${5:-`date +"%B, %Y"`}


# make problem directory
mkdir "$name"
# copy templates and helpful files
cp runme_template.py "$name/runme.py"
cp test_runme_template.py "$name/test_runme.py"
cp helpful.py "$name/helpful.py"


# fill-in problem info inside the templates
sed -i "" "s/--Problem Name--/$name/g" "$name/runme.py" "$name/test_runme.py"
sed -i "" "s/--Year--/$year/g" "$name/runme.py" "$name/test_runme.py"
sed -i "" "s/--Round--/$round/g" "$name/runme.py" "$name/test_runme.py"
sed -i "" "s,--Link--,$link,g" "$name/runme.py" "$name/test_runme.py"
sed -i "" "s/--Date--/$date/g" "$name/runme.py" "$name/test_runme.py"
