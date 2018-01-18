package org.campllc.mbrbuilder.service;

import java.util.ArrayList;

import org.apache.commons.codec.binary.Hex;
import org.campllc.mbrbuilder.objects.CurvePoint;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class PseudonymSigningService {
	public class PseudonymSigningResult {
		public String rSig;
		public String sSig;
		public String digest;
		public int yPoint;
	}

	@Autowired
	ASNEncoder asnEncoder;

	@Autowired
	private PythonRunner pythonRunner;

	@Autowired
	private CertificateReaderService certificateReaderService;

	public PseudonymSigningResult signPayload(byte[] tbs, String certDir, String certGroup, String certNumber, String pcaFile) {
		PseudonymSigningResult returnData = new PseudonymSigningResult();
		// read in the PCS cert
		CurvePoint certificateResult =  certificateReaderService.readCertificateVerificationKeyFromFile(pcaFile);
		// run the python script to get signature information
		ArrayList<String> arguments = new ArrayList<>();
		arguments.add("-f");
		arguments.add(certDir);
		arguments.add("-i");
		arguments.add(certGroup);
		arguments.add("-j");
		arguments.add(certNumber);
		arguments.add("--pcaFile");
		arguments.add(pcaFile);
		arguments.add("--pcaYPoint");
		arguments.add(Integer.toString(certificateResult.getyPoint()));
		arguments.add("-p");
		arguments.add(Hex.encodeHexString(certificateResult.getyValue()));
		arguments.add("-b");
		arguments.add(Hex.encodeHexString(tbs));
		String[] output = pythonRunner.runPythonScript("pseudonym_sign.py", arguments);
		returnData.rSig = output[0].substring(20,84);
		returnData.sSig = output[1].substring(2);
		returnData.digest = output[2];
		returnData.yPoint = certificateResult.getyPoint();
		return returnData;
	}
}
