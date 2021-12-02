# Software Install Instructions

This package is supported for Windows 32-bit python, due to dependencies linking to the Ultrasonix US machines.
You may not have 32-bit 3.7.9 python natively installed in you machine, so you may need to install it first. If you do have native

## Installing 32-bit 3.7.9 Python on your machine

From a bash terminal, get the installer.

```bash
wget https://www.python.org/ftp/python/3.7.9/python-3.7.9.exe
```

Run the installer and note the path to the python, henceforth referred to as `/path/to/python32_37/`.

## Making a 32-bit 3.7.9 Python virtualenv

### Deactivating Conda
In the case that you use `conda` for environment management, you may need to run this command first:

```bash
source /path/to/conda/Scripts/deactivate
```

Where `/path/to/conda/` is your own path to your anaconda/miniconda installation.

### Making a virtualenv
Make a 32-bit python virtualenv, and activate it by running the following:

```bash
/path/to/python32_37/python -m pip install virtualenv
/path/to/python32_37/python -m venv /path/to/desired/venv/location/venv_name/
source /path/to/desired/venv/location/venv_name/Scripts/activate
```

Then, install requirements as usual using `pip`.

```bash
pip install -r requirements.txt
```

## Installing 32-bit Ultrasonix DLLs

Navigate to the `scikitsurgerytrackedvidus` repository, and download the DLLs to interface with the Ultrasonix machine like:

```bash
wget ultrasonix.zip <url with Ultrasonix DLLs>
unzip ultrasonix.zip
```

## Installing the package

```bash
pip install -e .
```

# Hardware Install Instructions

You'll need:

- Two Ethernet ports
- Ultrasonix Machine
- NDI Tracker

## US IP setting

To ensure that your computer can interface with the Ultrasonix, you must connect the Ultrasonix ethernet cable to your machine.
The Ultrasonix machine has an IP address, note this down, as it has to be used programmatically in the config file to grab data.

On Windows, you can search for Ethernet under the Network tab, navigate to "change adapter options", then "find connection".

For one of the Ethernet connections on your machine, make sure that the IP address is appropriate to communicate with the Ultrasonix.
Change IP address in "Internet Protocol Version 4":
- First field has to be the same first two numbers as the machine, eg if machine is "128.16.0.3", first field should be "128.16.0.X"
- Second field (subnet mask) "255.255.255.X"

## NDI IP setting

You must also connect the NDI ethernet cable to your machine, and note it's IP address.

Follow the same instructions as above, and modify the other Ethernet connection on your machine using the NDI address.
