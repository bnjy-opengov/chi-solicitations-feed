if [ -d "vEnv" ];
then
  	echo "vEnv exists"
else
	virtualenv --distribute vEnv
fi
source vEnv/bin/activate
pip install -r requirements.txt