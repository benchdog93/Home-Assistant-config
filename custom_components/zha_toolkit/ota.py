import logging

LOGGER = logging.getLogger(__name__)


async def ota_notify(
    app, listener, ieee, cmd, data, service, params, event_data
):
    if ieee is None:
        LOGGER.error("missing ieee")
        return

    LOGGER.debug("running 'image_notify' command: %s", service)

    device = app.get_device(ieee=ieee)

    cluster = None
    for epid, ep in device.endpoints.items():
        if epid == 0:
            continue
        if 0x0019 in ep.out_clusters:
            cluster = ep.out_clusters[0x0019]
            break
    if cluster is None:
        LOGGER.debug("No OTA cluster found")
        return
    basic = device.endpoints[cluster.endpoint.endpoint_id].basic
    await basic.bind()
    ret = await basic.configure_reporting("sw_build_id", 0, 1800, 1)
    LOGGER.debug("Configured reporting: %s", ret)
    ret = await cluster.image_notify(0, 100)

    LOGGER.debug("Sent image notify command to 0x%04x: %s", device.nwk, ret)
