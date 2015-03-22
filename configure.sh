echo "Please, type your password to configure AES Helper"
sudo easy_install virtualenv
echo "|||||||||||||||||||||||||||||||||||||"
echo "||                                 ||"
echo "||      Configuration Started!     ||"
echo "||                                 ||"
echo "|||||||||||||||||||||||||||||||||||||"
virtualenv venv
source venv/bin/activate
pip install -r requeriments.txt

echo "Testing the algorithm..."
python tests.py 1000
echo "|||||||||||||||||||||||||||||||||||||"
echo "||                                 ||"
echo "||     Configuration Finished!     ||"
echo "||                                 ||"
echo "|||||||||||||||||||||||||||||||||||||"
