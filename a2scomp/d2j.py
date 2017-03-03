import subprocess
import sys

import click

from a2scomp.a2scomp import cli


@cli.command()
@click.pass_obj
def jarify(config):
    if config.apk:
        click.echo('Going to jarify the APK...')

        try:
            subprocess.run(['d2j-dex2jar', config.apk],
                           stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL).check_returncode()
        except subprocess.CalledProcessError:
            print('[-] The APK can\'t be jarified')
            sys.exit()

        click.echo('[+] Succesfully jarified the APK')
    else:
        click.echo('[-] No APK provided')
