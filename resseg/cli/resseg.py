# -*- coding: utf-8 -*-

"""Console script for resseg."""
import sys
import click


INPUT_FILE_TYPE = click.Path(exists=True, dir_okay=False)
OUTPUT_FILE_TYPE = click.Path(dir_okay=False)

@click.command()
@click.argument('input-path', type=INPUT_FILE_TYPE)
@click.option(
    '--output-path', '-o',
    type=OUTPUT_FILE_TYPE,
)
@click.option(
    '--tta-iterations', '-a',
    type=int,
    default=6,
    show_default=True,
)
@click.option(
    '--interpolation', '-i',
    type=str,
    default='bspline',
    show_default=True,
)
@click.option(
    '--num_workers', '-j',
    type=int,
    default=0,
    show_default=True,
)
@click.option(
    '--postprocess/--raw',
    default=True,
    show_default=True,
)
@click.option(
    '--seed', '-s',
    type=int,
)
def main(
        input_path,
        output_path,
        tta_iterations,
        interpolation,
        num_workers,
        postprocess,
        seed,
        ):
    """Console script for resseg."""
    from resseg import resseg
    if seed is not None:
        import torch
        torch.manual_seed(seed)
    resseg(
        input_path,
        output_path,
        tta_iterations,
        interpolation,
        num_workers,
        postprocess=postprocess,
    )
    return 0


if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    sys.exit(main())  # pragma: no cover
