import subprocess
import sys

import click

from a2scomp.a2scomp import cli


@cli.command()
@click.pass_obj
def javafy(config):
    if config.apk:
        click.echo('Going to turn the APK into Java...')

        try:
            subprocess.run(['jadx', config.apk], stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL)
        except subprocess.CalledProcessError:
            print('[-] The APK couldn\'t be converted to Java')
            sys.exit()

        click.echo('[+] Successfully turned APK into Java...')
    else:
        click.echo('[-] No APK provided')
        sys.exit()
