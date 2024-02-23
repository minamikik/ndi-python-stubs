from enum import IntEnum
from typing import List, Optional, Tuple

import numpy as np

class FrameType(IntEnum):
    FRAME_TYPE_NONE = ...
    FRAME_TYPE_VIDEO = ...
    FRAME_TYPE_AUDIO = ...
    FRAME_TYPE_METADATA = ...
    FRAME_TYPE_ERROR = ...
    FRANE_TYPE_STATUS_CHANGE = ...
    FRAME_TYPE_MAX = ...

class FourCCVideoType(IntEnum):
    FOURCC_VIDEO_TYPE_UYVY = ...
    FOURCC_VIDEO_TYPE_UYVA = ...
    FOURCC_VIDEO_TYPE_P216 = ...
    FOURCC_VIDEO_TYPE_PA16 = ...
    FOURCC_VIDEO_TYPE_YV12 = ...
    FOURCC_VIDEO_TYPE_I420 = ...
    FOURCC_VIDEO_TYPE_NV12 = ...
    FOURCC_VIDEO_TYPE_BGRA = ...
    FOURCC_VIDEO_TYPE_BGRX = ...
    FOURCC_VIDEO_TYPE_RGBA = ...
    FOURCC_VIDEO_TYPE_RGBX = ...
    FOURCC_VIDEO_TYPE_MAX = ...

class FourCCAudioType(IntEnum):
    FOURCC_AUDIO_TYPE_FLTP = ...
    FOURCC_AUDIO_TYPE_MAX = ...

class FrameFormatType(IntEnum):
    FRAME_FORMAT_TYPE_PROGRESSIVE = ...
    FRAME_FORMAT_TYPE_INTERLEAVED = ...
    FRAME_FORMAT_TYPE_FIELD_0 = ...
    FRAME_FORMAT_TYPE_FIELD_1 = ...
    FRAME_FORMAT_TYPE_MAX = ...

class RecvBandwidth(IntEnum):
    RECV_BANDWIDTH_METADATA_ONLY = ...
    RECV_BANDWIDTH_AUDIO_ONLY = ...
    RECV_BANDWIDTH_LOWEST = ...
    RECV_BANDWIDTH_HIGHEST = ...
    RECV_BANDWIDTH_MAX = ...

class RecvColorFormat(IntEnum):
    RECV_COLOR_FORMAT_BGRX_BGRA = ...
    RECV_COLOR_FORMAT_UYVY_BGRA = ...
    RECV_COLOR_FORMAT_RGBX_RGBA = ...
    RECV_COLOR_FORMAT_UYVY_RGBA = ...
    RECV_COLOR_FORMAT_FASTEST = ...
    RECV_COLOR_FORMAT_BEST = ...
    RECV_COLOR_FORMAT_E_BGRX_BGRA = ...
    RECV_COLOR_FORMAT_E_UYVY_BGRA = ...
    RECV_COLOR_FORMAT_E_RGBX_RGBA = ...
    RECV_COLOR_FORMAT_E_UYVY_RGBA = ...
    RECV_COLOR_FORMAT_MAX = ...
    # for Windows only
    RECV_COLOR_FORMAT_BGRX_BGRA_FLIPPED = ...

class Source:
    p_ndi_name: Optional[str]
    p_url_address: Optional[str]

    def __init__(self, p_ndi_name: Optional[str] = None, p_url_address: Optional[str] = None) -> None: ...

class VideoFrameV2:
    xres: int
    yres: int
    FourCC: FourCCVideoType
    frame_rate_N: int
    frame_rate_D: int
    picture_aspect_ratio: float
    frame_format_type: FrameFormatType
    timecode: int
    p_data: Optional[np.ndarray]
    line_stride_in_bytes: int
    p_metadata: Optional[str]
    timestamp: int

    def __init__(
        self,
        xres: int = 0,
        yres: int = 0,
        FourCC: FourCCVideoType = FourCCVideoType.FOURCC_VIDEO_TYPE_UYVY,
        frame_rate_N: int = 30000,
        frame_rate_D: int = 1001,
        picture_aspect_ratio: float = 0.0,
        frame_format_type: FrameFormatType = FrameFormatType.FRAME_FORMAT_TYPE_PROGRESSIVE,
        timecode: int = 0,
        p_data: Optional[np.ndarray] = None,
        line_stride_in_bytes: int = 0,
        p_metadata: Optional[str] = None,
        timestamp: int = 0,
    ) -> None: ...

class AudioFrameV2:
    sample_rate: int
    no_channels: int
    no_samples: int
    timecode: int
    p_data: Optional[np.ndarray]
    channel_stride_in_bytes: int
    p_metadata: Optional[str]
    timestamp: int

    def __init__(
        self,
        sample_rate: int = 48000,
        no_channels: int = 2,
        no_samples: int = 0,
        timecode: int = 0,
        p_data: Optional[np.ndarray] = None,
        channel_stride_in_bytes: int = 0,
        p_metadata: Optional[str] = None,
        timestamp: int = 0,
    ) -> None: ...

class AudioFrameV3:
    sample_rate: int
    no_channels: int
    no_samples: int
    timecode: int
    FourCC: FourCCAudioType
    p_data: Optional[np.ndarray]
    channel_stride_in_bytes: int
    p_metadata: Optional[str]
    timestamp: int

    def __init__(
        self,
        sample_rate: int = 48000,
        no_channels: int = 2,
        no_samples: int = 0,
        timecode: int = 0,
        FourCC: FourCCAudioType = FourCCAudioType.FOURCC_AUDIO_TYPE_FLTP,
        p_data: Optional[np.ndarray] = None,
        channel_stride_in_bytes: int = 0,
        p_metadata: Optional[str] = None,
        timestamp: int = 0,
    ) -> None: ...

class MetadataFrame:
    length: int
    timecode: int
    p_data: Optional[str]

    def __init__(self, length: int = 0, timecode: int = 0, p_data: Optional[str] = None) -> None: ...

class Tally:
    on_program: bool
    on_preview: bool

    def __init__(self, on_program: bool = False, on_preview: bool = False) -> None: ...

class FindCreate:
    show_local_sources: bool
    p_groups: Optional[str]
    p_extra_ips: Optional[str]

    def __init__(
        self, show_local_sources: bool = True, p_groups: Optional[str] = None, p_extra_ips: Optional[str] = None
    ) -> None: ...

class RecvCreateV3:
    source_to_connect_to: Source
    color_format: RecvColorFormat
    bandwidth: RecvBandwidth
    allow_video_fields: bool
    p_ndi_recv_name: Optional[str]

    def __init__(
        self,
        source_to_connect_to: Source = Source(),
        color_format: RecvColorFormat = RecvColorFormat.RECV_COLOR_FORMAT_UYVY_BGRA,
        bandwidth: RecvBandwidth = RecvBandwidth.RECV_BANDWIDTH_HIGHEST,
        allow_video_fields: bool = True,
        p_ndi_recv_name: Optional[str] = None,
    ) -> None: ...

class SendCreate:
    p_ndi_name: Optional[str]
    p_groups: Optional[str]
    clock_video: bool
    clock_audio: bool

    def __init__(
        self,
        p_ndi_name: Optional[str] = None,
        p_groups: Optional[str] = None,
        clock_video: bool = True,
        clock_audio: bool = True,
    ) -> None: ...

class RoutingCreate:
    p_ndi_name: Optional[str]
    p_groups: Optional[str]

    def __init__(self, p_ndi_name: Optional[str] = None, p_groups: Optional[str] = None) -> None: ...

SEND_TIMECODE_SYNTHESIZE: int
RECV_TIMESTAMP_UNDEFINED: int

def initialize() -> bool:
    """Initializes the NDI library."""
    pass

def destroy() -> None:
    """Terminates the NDI library and releases resources."""
    pass

def version() -> str:
    """Retrieves the version of the NDI library."""
    pass

def is_supported_CPU() -> bool:
    """Checks if the current CPU supports the NDI library."""
    pass

def find_create_v2(create_settings: Optional[FindCreate] = None) -> object:
    """Creates an instance for detecting NDI sources."""
    pass

def find_destroy(instance: object) -> None:
    """Destroys the NDI source detection instance."""
    pass

def find_get_current_sources(instance: object) -> List[Source]:
    """Gets a list of currently detected NDI sources."""
    pass

def find_wait_for_sources(instance: object, timeout_in_ms: int) -> bool:
    """Waits until new NDI sources are detected."""
    pass

def recv_create_v3(create_settings: RecvCreateV3) -> object:
    """Creates an NDI receiving instance."""
    pass

def recv_destroy(instance: object) -> None:
    """Destroys the NDI receiving instance."""
    pass

def recv_connect(instance: object, source: Source) -> None:
    """Connects to a specified NDI source."""
    pass

def recv_capture_v2(
    instance: object, timeout_in_ms: int
) -> Tuple[Optional[VideoFrameV2], Optional[AudioFrameV2], Optional[MetadataFrame]]:
    """Captures video, audio, and metadata frames."""
    pass

def recv_capture_v3(
    instance: object, timeout_in_ms: int
) -> Tuple[Optional[VideoFrameV2], Optional[AudioFrameV3], Optional[MetadataFrame]]:
    """Captures video, audio (version 3), and metadata frames."""
    pass

def recv_free_video_v2(instance: object, video_data: VideoFrameV2) -> None:
    """Frees memory of the video frame."""
    pass

def recv_free_audio_v2(instance: object, audio_data: AudioFrameV2) -> None:
    """Frees memory of the audio frame."""
    pass

def recv_free_audio_v3(instance: object, audio_data: AudioFrameV3) -> None:
    """Frees memory of the audio frame version 3."""
    pass

def recv_free_metadata(instance: object, metadata: MetadataFrame) -> None:
    """Frees memory of the metadata."""
    pass

def send_create(create_settings: SendCreate) -> object:
    """Creates an NDI sending instance."""
    pass

def send_destroy(instance: object) -> None:
    """Destroys the NDI sending instance."""
    pass

def send_send_video_v2(instance: object, video_data: VideoFrameV2) -> None:
    """Sends a video frame."""
    pass

def send_send_audio_v2(instance: object, audio_data: AudioFrameV2) -> None:
    """Sends an audio frame."""
    pass

def send_send_audio_v3(instance: object, audio_data: AudioFrameV3) -> None:
    """Sends Audio Frame Version 3."""
    pass

def send_send_metadata(instance: object, metadata: MetadataFrame) -> None:
    """Sends metadata."""
    pass

def send_capture(instance: object, metadata: MetadataFrame, timeout_in_ms: int) -> None:
    """Captures metadata."""
    pass

def send_free_metadata(instance: object, metadata: MetadataFrame) -> None:
    """Frees memory of metadata."""
    pass

def send_get_tally(instance: object, tally: Tally, timeout_in_ms: int) -> bool:
    """Gets tally information."""
    pass

def send_get_no_connections(instance: object, timeout_in_ms: int) -> int:
    """Gets the number of connections."""
    pass

def send_clear_connection_metadata(instance: object) -> None:
    """Clears connection metadata."""
    pass

def send_add_connection_metadata(instance: object, metadata: MetadataFrame) -> None:
    """Adds connection metadata."""
    pass

def send_set_failover(instance: object, failover_source: Source) -> None:
    """Sets failover source."""
    pass

def send_get_source_name(instance: object) -> str:
    """Gets the name of the sending source."""
    pass

def routing_create(create_settings: RoutingCreate) -> object:
    """Creates a routing instance."""
    pass

def routing_destroy(instance: object) -> None:
    """Destroys a routing instance."""
    pass

def routing_change(instance: object, source: Source) -> None:
    """Changes routing."""
    pass

def routing_clear(instance: object) -> None:
    """Clears routing configuration."""
    pass

def routing_get_no_connections(instance: object, timeout_in_ms: int) -> int:
    """Gets the number of routing connections."""
    pass

def routing_get_source_name(instance: object) -> str:
    """Gets the name of the routing source."""
    pass
