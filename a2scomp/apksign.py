import subprocess
import sys

import click

from a2scomp.a2scomp import cli


@cli.command()
@click.pass_obj
def sign(config):
    if config.apk:
        click.echo('Going to sign the APK...')

        try:
            apk_release = config.apk.split('/')[-1].split('.')
            apk_release[-2] += '-release'
            apk_release = '.'.join(apk_release)
            subprocess.run(['apksigner', 'sign', '--ks', config.keystore,
                            '--out', apk_release,
                            config.apk]).check_returncode()
        except subprocess.CalledProcessError:
            print('[-] Can\'t sign the APK')
            sys.exit()

        click.echo('[+] Succesfully signed the APK')
    else:
        click.echo('[-] No aligned APK provided')
        sys.exit()
