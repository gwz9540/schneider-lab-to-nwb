"""Primary NWBConverter class for this dataset."""
from neuroconv import NWBConverter
from neuroconv.datainterfaces import (
    PhySortingInterface,
    ExternalVideoInterface,
    SLEAPInterface,
)

from schneider_lab_to_nwb.corredera_2025 import (
    Corredera2025AudioInterface,
    Corredera2025StimulusInterface,
)


class Corredera2025NWBConverter(NWBConverter):
    """Primary conversion class."""

    data_interface_classes = dict(
        Video=ExternalVideoInterface,
        SLEAP=SLEAPInterface,
        Audio=Corredera2025AudioInterface,
        Stimulus=Corredera2025StimulusInterface,
    )
