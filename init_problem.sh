#!/bin/bash


if [ $# -ne 4 ]
then
  echo 'Usage: init_problem.sh "Problem Name" Year "Round" Link'
  exit 0
fi


name=${1:-DefaultProblemName}
year=${2:-DefaultYear}
round=${3:-DefaultRound}
link=${4:-DefaultLink}


mkdir "$name"
cp runme-template.py "$name/runme.py"
cp test_runme-template.py "$name/test_runme.py"
cp helpful.py "$name/helpful.py"


sed -i "" "s/--Problem Name--/$name/g" "$name/runme.py" "$name/test_runme.py"
sed -i "" "s/--Year--/$year/g" "$name/runme.py" "$name/test_runme.py"
sed -i "" "s/--Round--/$round/g" "$name/runme.py" "$name/test_runme.py"
sed -i "" "s,--Link--,$link,g" "$name/runme.py" "$name/test_runme.py"

