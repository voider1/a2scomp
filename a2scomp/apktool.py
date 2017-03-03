import subprocess
import sys
import shutil
import os

import click

from a2scomp.a2scomp import cli
from a2scomp import zipalign as align
from a2scomp import apksign


@cli.command()
@click.pass_obj
def decode(config):
    if config.apk:
        click.echo('Going to decode the APK...')

        try:
            subprocess.run(['apktool', 'd', '-f', '-r', '-c', config.apk],
                           stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL).check_returncode()
        except subprocess.CalledProcessError:
            print('[-] The APK can\'t be decoded')
            sys.exit()

        config.smali = config.apk.split('/')[-1][:-4]
        click.echo('[+] Succesfully decoded the APK')
    else:
        click.echo("[-] No APK provided")
        sys.exit()


@cli.command()
@click.option('--zipalign', is_flag=True,
              help='After building it, sign the APK')
@click.option('--sign', is_flag=True,
              help='After building and aligning it, sign the APK')
@click.pass_context
def build(ctx, zipalign, sign):
    config = ctx.obj

    if config.smali:
        click.echo('Going to build the APK...')

        try:
            subprocess.run(['apktool', 'b', config.smali],
                           stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL).check_returncode()
        except subprocess.CalledProcessError:
            print('[-] The APK can\'t be rebuild after decoding')
            sys.exit()

        click.echo('[+] Succesfully built the APK')

        if zipalign:
            config.apk = os.path.join(config.smali, 'dist', config.smali + '.apk')
            ctx.invoke(align.zipalign)

        if sign:
            ctx.invoke(apksign.sign)

        if config.clean:
            click.echo('Cleaning...')
            shutil.rmtree(config.smali)
    else:
        click.echo("[-] No smali provided")
        sys.exit()


@cli.command()
@click.option('--clean', is_flag=True,
              help='Removes all the (de)compiled code this command generated')
@click.pass_context
def test(ctx, clean):
    click.echo('Starting the test...')
    ctx.obj.clean = clean
    ctx.invoke(decode)
    ctx.invoke(build)
    click.echo('[+] Succesfully tested the APK')
