package org.campllc.mbrbuilder.service.mai;

import java.io.File;
import java.io.FileInputStream;
import java.io.InputStream;

import com.oss.asn1.OctetString;
import org.campllc.asn1.generatedmai.ieee1609dot2.Certificate;
import org.campllc.asn1.generatedmai.ieee1609dot2basetypes.EccP256CurvePoint;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class CertificateReaderServiceMAI {
	public class CertificateResult {
		int verifyKeyYPoint;
		OctetString verifyKeyData;
	}

	@Autowired
	private ASNEncoderMAI encoder;

	CertificateResult readCertificateVerificationKeyFromFile(String certFile) {
		CertificateResult certificateResult = new CertificateResult();
		try {
			InputStream inputStream = new FileInputStream(certFile);
			Certificate certificate = encoder.decodeCertificate(inputStream);
			EccP256CurvePoint curvePoint =	certificate.getToBeSigned().getVerifyKeyIndicator().getVerificationKey().getEcdsaNistP256();
			if (curvePoint.getCompressed_y_0() != null) {
				certificateResult.verifyKeyYPoint = 0;
				certificateResult.verifyKeyData = curvePoint.getCompressed_y_0();
			} else if (curvePoint.getCompressed_y_1() != null) {
				certificateResult.verifyKeyYPoint = 1;
				certificateResult.verifyKeyData = curvePoint.getCompressed_y_1();
			}
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
