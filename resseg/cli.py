# -*- coding: utf-8 -*-

"""Console script for resseg."""
import sys
import click

INPUT_FILE_TYPE = click.Path(exists=True, dir_okay=False)
OUTPUT_FILE_TYPE = click.Path(dir_okay=False)

@click.command()
@click.argument('input-path', type=INPUT_FILE_TYPE)
@click.argument('output-path', type=OUTPUT_FILE_TYPE)
@click.option(
    '--window_size', '-w',
    type=int,
    default=128,
    show_default=True,
)
@click.option(
    '--window_border', '-c',
    type=int,
    default=1,
    show_default=True,
)
@click.option(
    '--batch_size', '-b',
    type=int,
    default=1,
    show_default=True,
)
@click.option(
    '--whole-image/--patch-based',
    default=False,
    show_default=True,
)
def main(input_path, output_path, window_size, window_border, batch_size, whole_image):
    """Console script for resseg."""
    """
    For now, the image is assumed to have been preprocessed:
    1) Reg to MNI, RAS 1 mm iso
    2) Brain segmented
    3) Bias correction
    4) Histogram standardization
    5) Z-normalization
    """
    from resseg import resseg
    resseg(
        input_path,
        output_path,
        window_size,
        window_border,
        batch_size,
        whole_image=whole_image,
    )
    return 0


if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    sys.exit(main())  # pragma: no cover
