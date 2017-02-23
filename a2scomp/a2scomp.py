#!../venv/bin/python
import click

from config import Config


@click.group()
@click.option('--apk', type=click.Path(exists=True),
              help='APK to perform operation on')
@click.option('--smali', type=click.Path(exists=True),
              help='Smali to perform operation on')
@click.option('--keystore', type=click.Path(exists=True),
              help='Keystore to use for signing')
@click.pass_context
def cli(ctx, apk, smali, keystore):
    ctx.obj = Config(apk, smali, keystore)


import apktool  # NOQA
import zipalign  # NOQA
import apksign  # NOQA
import d2j  # NOQA
