"""Aerial position model."""

from auvsi_suas.models import distance
from django.db import models
from gps_position import GpsPosition


class AerialPosition(models.Model):
    """Aerial position which consists of a GPS position and an altitude."""
    # GPS position
    gps_position = models.ForeignKey(GpsPosition)
    # Altitude (MSL) in feet
    altitude_msl = models.FloatField()

    def __unicode__(self):
        """Descriptive text for use in displays."""
        return unicode("AerialPosition (pk:%s, alt:%s, gps:%s)" %
                       (str(self.pk), str(self.altitude_msl),
                        self.gps_position.__unicode__()))

    def distanceTo(self, other):
        """Computes distance to another position.

        Args:
          other: The other position.
        Returns:
          Distance in feet.
        """
        return distance.distanceTo(
            self.gps_position.latitude, self.gps_position.longitude,
            self.altitude_msl, other.gps_position.latitude,
            other.gps_position.longitude, other.altitude_msl)
