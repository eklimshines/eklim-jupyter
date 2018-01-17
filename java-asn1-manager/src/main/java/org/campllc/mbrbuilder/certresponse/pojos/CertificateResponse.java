package org.campllc.mbrbuilder.certresponse.pojos;

/**
 * If the iPeriod is not filled in then the system will attempt to process all files in the directory.
 */
public class CertificateResponse {
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
