package org.campllc.mbrbuilder.crlResponse;

import org.apache.commons.codec.binary.Hex;
import org.apache.commons.logging.Log;
import org.apache.commons.logging.LogFactory;
import org.campllc.mbrbuilder.processing.ProcessingTypes;
import org.campllc.mbrbuilder.processing.Processor;
import org.campllc.mbrbuilder.processing.ProcessorManager;
import org.campllc.mbrbuilder.service.*;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Component;
import org.campllc.asn1.generated.ieee1609dot2scmscomponentcertificatemanagement.CompositeCrl;
import org.campllc.asn1.generated.ieee1609dot2crl.SecuredCrl;

import java.io.*;


@Component
public class CRLResponseProcessor implements Processor {

    private static Log log = LogFactory.getLog(CRLResponseProcessor.class);

    @Value("${crl.outputPath}")
    String outPath;

    @Value("${crl.ListFile}")
    String CrlListFile;

    @Value("${crl.nameOfCrlFile}")
    String CrlFileName;

    @Autowired
    private JSONReader reader;

    @Autowired
    private ASNEncoder asnEncoder;

    @Autowired
    private SigningService signingService;

    @Autowired
    private EncryptionService encryptionService;

    @Autowired
    private PropertyService propertyService;

    public CRLResponseProcessor() {
        ProcessorManager.processorMap.put(getProcessorType(), CRLResponseProcessor.class);
    }

    @Override
    public ProcessingTypes getProcessorType() {
        return ProcessingTypes.crlResponse;
    }

    @Override
    public void runProcess() {
        try {
            log.info("Beginning conversion and encryption for crlResponse");
            File nameOfCrlfile = new File(CrlFileName);
            BufferedReader bufferedReader = new BufferedReader(new FileReader(nameOfCrlfile));
            String crlFilename = bufferedReader.readLine();
            File compositeCrlFile = new File(outPath+"\\"+crlFilename);
            FileInputStream compositeCrlData = new FileInputStream(compositeCrlFile);
            CompositeCrl compositeCrl = asnEncoder.decodeCompositeCrl(compositeCrlData);
            String readableCrlFileFullPath = outPath +"\\"+ "readable_crl_file.txt";
            PrintWriter printWriter = new PrintWriter(readableCrlFileFullPath);
            printWriter.println(compositeCrl);
            printWriter.close();
            log.info("The CRL file can be read at " + readableCrlFileFullPath);
            log.info("Process complete");
        } catch (Exception e) {
            throw new RuntimeException("Unable to process crlResponse message", e);
        }
    }

}