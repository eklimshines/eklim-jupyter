package org.campllc.mbrbuilder.service;

import com.oss.asn1.AbstractData;
import com.oss.asn1.Coder;
import com.oss.asn1.DecodeFailedException;
import com.oss.asn1.DecodeNotSupportedException;
import org.campllc.asn1.generated.Generated;
import org.campllc.asn1.generated.ieee1609dot2.Certificate;
import org.campllc.asn1.generated.ieee1609dot2.Ieee1609Dot2Data;
import org.campllc.asn1.generated.ieee1609dot2.ToBeSignedData;
import org.campllc.asn1.generated.ieee1609dot2basetypes.SymmetricEncryptionKey;
import org.campllc.asn1.generated.ieee1609dot2endentitymainterface.EndEntityMaInterfacePDU;
import org.campllc.asn1.generated.ieee1609dot2endentitymainterfacembrbuilder.CertificatePDU;
import org.campllc.asn1.generated.ieee1609dot2endentitymainterfacembrbuilder.ToBeSignedDataPDU;
import org.campllc.asn1.generated.ieee1609dot2pcarainterface.DecryptedCertificateData;
import org.campllc.asn1.generated.ieee1609dot2scmsprotocol.ScopedLocalCertificateChainFile;
import org.campllc.asn1.generated.ieee1609dot2scmsprotocol.SignedEeEnrollmentCertResponse;
import org.campllc.asn1.generated.ieee1609dot2scmsprotocol.SignedPseudonymCertProvisioningAck;
import org.campllc.asn1.generated.ieee1609dot2scmscomponentcertificatemanagement.CompositeCrl;
import org.campllc.asn1.generatedmai.ieee1609dot2scmsbasetypes.ToBeEncryptedIndividualPLV;
import org.campllc.mbrbuilder.objects.CommMsg;
import org.springframework.stereotype.Service;

import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.InputStream;

/**
 * Created by Griff Baily on 6/19/2017.
 */
@Service
public class ASNEncoder {
    public ASNEncoder()
    {

    }

    public CompositeCrl decodeCompositeCrl (InputStream inputStream) throws DecodeNotSupportedException, DecodeFailedException {
        Coder coder = Generated.getOERCoder();
        coder.enableAutomaticDecoding();
        CompositeCrl crlList = (CompositeCrl) coder.decode(inputStream, new CompositeCrl());
        return crlList;
    }

    public ToBeEncryptedIndividualPLV decodeToBeEncryptedIndividualPLV (InputStream inputStream) throws DecodeNotSupportedException, DecodeFailedException {
        Coder coder = Generated.getOERCoder();
        coder.enableAutomaticDecoding();
        ToBeEncryptedIndividualPLV toBeEncryptedIndividualPLV = (ToBeEncryptedIndividualPLV) coder.decode(inputStream, new ToBeEncryptedIndividualPLV());
        return toBeEncryptedIndividualPLV;
    }

    public Certificate decodeCertificate(InputStream inputStream) throws DecodeNotSupportedException, DecodeFailedException {
        Coder coder = Generated.getOERCoder();
        coder.enableAutomaticDecoding();
        CertificatePDU cert = (CertificatePDU) coder.decode(inputStream, new CertificatePDU());
        return cert;
    }

    public ScopedLocalCertificateChainFile decodeCertificateChainFile(byte[] bytes) throws DecodeNotSupportedException, DecodeFailedException {
        Coder coder = Generated.getOERCoder();
        coder.enableAutomaticDecoding();
        ByteArrayInputStream inputStream = new ByteArrayInputStream(bytes);
        ScopedLocalCertificateChainFile asnObject = (ScopedLocalCertificateChainFile) coder.decode(inputStream, new ScopedLocalCertificateChainFile());
        return asnObject;
    }

    public SignedEeEnrollmentCertResponse decodeCertificateResponse(byte[] bytes) throws DecodeNotSupportedException, DecodeFailedException {
        Coder coder = Generated.getOERCoder();
        coder.enableAutomaticDecoding();
        ByteArrayInputStream inputStream = new ByteArrayInputStream(bytes);
        SignedEeEnrollmentCertResponse asnObject = (SignedEeEnrollmentCertResponse) coder.decode(inputStream, new SignedEeEnrollmentCertResponse());
        return asnObject;
    }

    public DecryptedCertificateData decodeDecryptedCertificateData(byte[] decryptedCertificateDataBytes) throws DecodeNotSupportedException, DecodeFailedException {
        Coder coder = Generated.getOERCoder();
        coder.enableAutomaticDecoding();
        ByteArrayInputStream inputStream = new ByteArrayInputStream(decryptedCertificateDataBytes);
        return  (DecryptedCertificateData) coder.decode(inputStream, new DecryptedCertificateData());
    }

    public SignedPseudonymCertProvisioningAck decodeProvisioningAck(byte[] bytes) throws DecodeNotSupportedException, DecodeFailedException {
        Coder coder = Generated.getOERCoder();
        coder.enableAutomaticDecoding();
        ByteArrayInputStream inputStream = new ByteArrayInputStream(bytes);
        SignedPseudonymCertProvisioningAck asnObject = (SignedPseudonymCertProvisioningAck) coder.decode(inputStream, new SignedPseudonymCertProvisioningAck());
        return asnObject;
    }

    public EndEntityMaInterfacePDU decodeEeMaPdu(CommMsg msg) throws Exception {
        Coder coder = Generated.getOERCoder();
        coder.enableAutomaticDecoding();
        ByteArrayInputStream inputStream = new ByteArrayInputStream(msg.getMsg());
        EndEntityMaInterfacePDU endEntity = (EndEntityMaInterfacePDU) coder.decode(inputStream, new EndEntityMaInterfacePDU());
        return endEntity;
    }

    public Ieee1609Dot2Data decodeIeeeData(CommMsg msg) throws Exception {
        Coder coder = Generated.getOERCoder();
        coder.enableAutomaticDecoding();
        ByteArrayInputStream inputStream = new ByteArrayInputStream(msg.getMsg());
        Ieee1609Dot2Data out = (Ieee1609Dot2Data) coder.decode(inputStream, new Ieee1609Dot2Data());
        return out;
    }

    public CommMsg simpleEncode(AbstractData data) throws Exception
    {
        Coder coder = Generated.getOERCoder();
        coder.enableAutomaticEncoding();
        ByteArrayOutputStream outputStream = new ByteArrayOutputStream();
        coder.encode(data, outputStream);
        CommMsg commMsg = new CommMsg(outputStream.toByteArray());
        return commMsg;
    }

    public CommMsg encodeTBSData(ToBeSignedData tbs)
    {
        Coder coder = Generated.getOERCoder();
        coder.enableAutomaticEncoding();
        ToBeSignedDataPDU endEntity= new ToBeSignedDataPDU();
        endEntity.setHeaderInfo(tbs.getHeaderInfo());
        endEntity.setPayload(tbs.getPayload());
        ByteArrayOutputStream outputStream = new ByteArrayOutputStream();
        try {
            coder.encode(endEntity, outputStream);
        }catch(Exception e)
        {
            e.printStackTrace();
        }
        CommMsg msg= new CommMsg(outputStream.toByteArray());
        return msg;
    }


}
