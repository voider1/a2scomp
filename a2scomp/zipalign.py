import subprocess
import sys

import click

from a2scomp.a2scomp import cli
from a2scomp import apksign


@cli.command()
@click.option('--sign', is_flag=True,
              help='After aligning it, sign the APK')
@click.pass_context
def zipalign(ctx, sign):
    config = ctx.obj

    if config.apk:
        click.echo('Going to zip align the APK...')

        try:
            apk_aligned = config.apk.split('/')[-1].split('.')
            apk_aligned[-2] += '-aligned'
            apk_aligned = '.'.join(apk_aligned)

            subprocess.run(['zipalign', '-v', '-p', '4', config.apk,
                            apk_aligned],
                           stdout=subprocess.DEVNULL).check_returncode()
        except subprocess.CalledProcessError:
            print('[-] The APK can\'t be zip aligned')
            sys.exit()

        click.echo('[+] Succesfully zip aligned the APK')

        if sign:
            config.apk = apk_aligned
            ctx.invoke(apksign.sign)
    else:
        click.echo("[-] No APK provided")
        sys.exit()
