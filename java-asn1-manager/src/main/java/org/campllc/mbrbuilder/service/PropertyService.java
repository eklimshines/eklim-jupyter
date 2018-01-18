package org.campllc.mbrbuilder.service;

import java.io.File;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;

@Service
public class PropertyService {
	@Value("${controlFile}")
	private String controlFile;

	@Value("${vehicleDirectory}")
	private String vehicleDirectory;

	@Value("${componentCertificateDirectory}")
	private String componentCertificateDirectory;

	@Value("${componentCertificateType}")
	private String componentCertificateType;

	@Value("${sharedFilesDirectory}")
	private String sharedFilesDirectory;

	public String getControlFile() {
		return controlFile;
	}

	public String getVehicleDirectory() {
		return vehicleDirectory;
	}

	public String getComponentCertificateType() {
		return componentCertificateType;
	}

	public String getSharedFilesDirectory() {
		return sharedFilesDirectory;
	}

	public File getComponentCertificateDirectory() {
		return new File(componentCertificateDirectory);
	}

	public File getComponentCertificateFile(String componentType) {
		File certificateDirectoryFile = getComponentCertificateDirectory();
		if (!certificateDirectoryFile.isDirectory()) {
			throw new RuntimeException("Certificate directory " + componentCertificateDirectory + " does not exist or is not a directory!");
		}
		return new File(certificateDirectoryFile, componentType + componentCertificateType + ".cert");
	}

	public File getComponentSigningPrivateKeyFile(String componentType) {
		File certificateDirectoryFile = getComponentCertificateDirectory();
		if (!certificateDirectoryFile.isDirectory()) {
			throw new RuntimeException("Certificate directory " + componentCertificateDirectory + " does not exist or is not a directory!");
		}
		return new File(certificateDirectoryFile, componentType + "-sgn" + componentCertificateType + ".priv");
	}

	public File getComponentEncryptionPrivateKeyFile(String componentType) {
		File certificateDirectoryFile = getComponentCertificateDirectory();
		if (!certificateDirectoryFile.isDirectory()) {
			throw new RuntimeException("Certificate directory " + componentCertificateDirectory + " does not exist or is not a directory!");
		}
		return new File(certificateDirectoryFile, componentType + "-enc" + componentCertificateType + ".priv");
	}
}
