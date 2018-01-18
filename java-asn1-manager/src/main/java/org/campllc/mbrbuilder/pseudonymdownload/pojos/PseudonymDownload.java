package org.campllc.mbrbuilder.pseudonymdownload.pojos;

/**
 * The iPeriod value is optional.  If not used then the current date is used as the starting point.
 */
public class PseudonymDownload {
	private String vehicleId;
	private String iPeriod;
	private int numberOfPeriods;

	public String getVehicleId() {
		return vehicleId;
	}

	public void setVehicleId(String vehicleId) {
		this.vehicleId = vehicleId;
	}

	public String getiPeriod() {
		return iPeriod;
	}

	public void setiPeriod(String iPeriod) {
		this.iPeriod = iPeriod;
	}

	public int getNumberOfPeriods() {
		return numberOfPeriods;
	}

	public void setNumberOfPeriods(int numberOfPeriods) {
		this.numberOfPeriods = numberOfPeriods;
	}
}
