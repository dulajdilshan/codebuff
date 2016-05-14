package org.antlr.codebuff.validation;

import org.antlr.codebuff.Formatter;
import org.antlr.v4.runtime.misc.Triple;

import java.util.List;

import static org.antlr.codebuff.Tool.SQLITE_CLEAN_DESCR;

public class FormatSQLite {
	public static void main(String[] args) throws Exception {
		LeaveOneOutValidator validator = new LeaveOneOutValidator("corpus/sql/training", SQLITE_CLEAN_DESCR);
		Triple<List<Formatter>,List<Float>,List<Float>> results = validator.validateDocuments(false, "output");
		System.out.println(results.b);
		System.out.println(results.c);
	}
}