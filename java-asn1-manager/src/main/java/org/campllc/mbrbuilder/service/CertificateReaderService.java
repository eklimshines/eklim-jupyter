package org.campllc.mbrbuilder.service;

import java.io.File;
import java.io.FileInputStream;
import java.io.InputStream;

import org.campllc.asn1.generated.ieee1609dot2.Certificate;
import org.campllc.asn1.generated.ieee1609dot2basetypes.EccP256CurvePoint;
import org.campllc.mbrbuilder.objects.CurvePoint;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class CertificateReaderService {

	@Autowired
	private ASNEncoder encoder;

	CurvePoint readCertificateVerificationKeyFromFile(String certFile) {
		CurvePoint certificateResult = new CurvePoint();
		try {
			InputStream inputStream = new FileInputStream(certFile);
			Certificate certificate = encoder.decodeCertificate(inputStream);
			EccP256CurvePoint curvePoint =	certificate.getToBeSigned().getVerifyKeyIndicator().getVerificationKey().getEcdsaNistP256();
			certificateResult.readFromEccP256CurvePoint(curvePoint);
		} catch (Exception e) {
			throw new RuntimeException(e);
		}
		return certificateResult;
	}

	public Certificate readCertificateFromFile(String fileName)  {
		try {
			InputStream inputStream = new FileInputStream(fileName);
			return encoder.decodeCertificate(inputStream);
		} catch (Exception e) {
			throw new RuntimeException(e);
		}
	}

	public Certificate readPseudonymCertificate(String certificateDirectory, String certificateGroup, String certificateNumber) {
		File file = new File(certificateDirectory + "/download/" + certificateGroup
				+ "/" + certificateGroup.toUpperCase() + "_" + certificateNumber + ".cert");
		return  readCertificateFromFile(file.getAbsolutePath());
	}
}
