#!/usr/bin/env bash
# Creates the boiler plate/template for the scripts to avoid constantly rewritting the same thing

touch $1
echo "#!/usr/bin/env bash" > $1
echo -e "#\n#+" >> $1
