package org.campllc.mbrbuilder.enrollment.pojos;

/**
 * If validUntil is filled in we attempt to make our enrollment valid until as close to that date as possible.
 * The format of the string is like this: "2007-12-03T10:15:30.00Z"
 */
public class Enrollment {
	private String vehicleId;
	private String validUntil;

	public String getVehicleId() {
		return vehicleId;
	}

	public void setVehicleId(String vehicleId) {
		this.vehicleId = vehicleId;
	}

	public String getValidUntil() {
		return validUntil;
	}

	public void setValidUntil(String validUntil) {
		this.validUntil = validUntil;
	}
}
