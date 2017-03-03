#!../venv/bin/python
import subprocess
import sys

import click

from config import Config


def test():
    try:
        subprocess.run(['apktool'], stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL).check_returncode()
    except subprocess.CalledProcessError:
        return False
        click.echo('[-] Apktool not found in path')

    try:
        if subprocess.run(['zipalign'], stdout=subprocess.DEVNULL,
                          stderr=subprocess.DEVNULL).returncode != 2:
            raise subprocess.CalledProcessError('Code for zipalign is not 2')
    except subprocess.CalledProcessError:
        return False
        click.echo('[-] Zipalign not found in path')

    try:
        subprocess.run(['apksigner'], stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL).check_returncode()
    except subprocess.CalledProcessError:
        return False
        click.echo('[-] Apksigner not found in path')

    try:
        subprocess.run(['d2j-dex2jar'],
                       stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL).check_returncode()
    except subprocess.CalledProcessError:
        return False
        click.echo('[-] Dex2jar not found in path')

    return True


@click.group()
@click.option('--apk', type=click.Path(exists=True),
              help='APK to perform operation on')
@click.option('--smali', type=click.Path(exists=True),
              help='Smali to perform operation on')
@click.option('--keystore', type=click.Path(exists=True),
              help='Keystore to use for signing')
@click.pass_context
def cli(ctx, apk, smali, keystore):
    if not test():
        sys.exit()
    ctx.obj = Config(apk, smali, keystore)


import apktool  # NOQA
import zipalign  # NOQA
import apksign  # NOQA
import d2j  # NOQA
