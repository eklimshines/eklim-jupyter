package org.campllc.mbrbuilder.service;

import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.stream.Collectors;

import org.apache.commons.logging.Log;
import org.apache.commons.logging.LogFactory;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;

@Service
public class PythonRunner {
	private static Log log = LogFactory.getLog(PythonRunner.class);

	public String[] runPythonScript(String pythonScriptName, ArrayList<String> arguments) {
		try {
			arguments.add(0, "python");
			arguments.add(1, "-m"); // find it in the path
			arguments.add(2, pythonScriptName);
			String[] command = arguments.toArray(new String[arguments.size()]);
			log.info("python command=" + Arrays.stream(command).map(n -> n.toString() )
					.collect( Collectors.joining( " " ) ));
			Process p = Runtime.getRuntime().exec(command);
			StreamGobbler errorGobbler = new
					StreamGobbler(p.getErrorStream(), "ERROR");
			StreamGobbler outputGobbler = new
					StreamGobbler(p.getInputStream(), "OUTPUT");
			new Thread(errorGobbler).start();
			new Thread(outputGobbler).start();
			p.waitFor();
			String[] output = outputGobbler.getOutput();
			if (output.length == 0) {
				log.error("Python script did not return a value.");
				for (String nextError : errorGobbler.getOutput()) {
					log.error("PYTHON ERRROR: " + nextError);
				}
				throw new RuntimeException("Python error, check logs");
			} else {
				for (String nextLine : output) {
					log.info("output: " + nextLine);
				}
			}
			return output;
		} catch (IOException e) {
			throw new RuntimeException(e);
		} catch (InterruptedException e) {
			throw new RuntimeException(e);
		}
	}
}
