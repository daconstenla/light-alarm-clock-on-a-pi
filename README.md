# my personal led matrix project

Source code of the python library is [jgarff/rpi_ws281x](https://github.com/jgarff/rpi_ws281x) and source code of the C library of adafruit neopixel [adafruit/Adafruit_NeoPixel](https://github.com/adafruit/Adafruit_NeoPixel).

## get it running

To prepare the environment you might need to run a couple of commands first:

```bash
# as root since adafruit library and pin configuration requires root access
source prepare-the-env.sh
# check if there is some dependency missing
verify_dependencies
# build C (if is not built) and install the python library for the examples to run
ws2812_build_and_install_package
# you can run the main C bin using `./test`, eg:
./test --width 6 --height 5 -g 18 --clear
# if you want to try some examples just run
ws2812_open_samples
# and then trigger one as could be `strandtest.py`
python strandtest.py
```
